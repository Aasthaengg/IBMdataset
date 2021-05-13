from sys import stdin


def main():
    from collections import deque

    _in = [_.rstrip() for _ in stdin.readlines()]
    N, M = list(map(int,_in[0].split(' ')))  # type:list(int)
    
    if M == 0:
        TF = 'Yes'
    else:
        L_R_D_arr = deque([])
        for i in range(M):
            _ = list(map(int,_in[i+1].split(' ')))  # type:list(int)
            L_R_D_arr.append(_)
        # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        iter_ = [float('inf')]*(N+1)
        iter_[L_R_D_arr[0][0]] = 0

        TF = 'No'
        rot_cnt = 0
        while len(L_R_D_arr)>0:
            if rot_cnt > len(L_R_D_arr):
                iter_ = [float('inf')]*(N+1)
                iter_[L_R_D_arr[0][0]] = 0
            else:
                L, R, D = L_R_D_arr[0]
                if iter_[L] == float('inf'):
                    if iter_[R] == float('inf'):
                        L_R_D_arr.rotate(-1)
                        rot_cnt += 1
                    else:
                        iter_[L] = iter_[R]-D
                        L_R_D_arr.popleft()
                        rot_cnt = 0
                else:
                    rot_cnt = 0
                    if iter_[R] == float('inf'):
                        iter_[R] = iter_[L]+D
                        L_R_D_arr.popleft()
                    elif iter_[R] == iter_[L]+D:
                        L_R_D_arr.popleft()
                    else:
                        break
        else:
            TF = 'Yes'
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(TF)


# 重み付きUnion-Find木
class Weighted_Union_Find():
    def __init__(self, N=1, SUM_UNITY=0):
        self.par  = [i for i in range(N)]  # 親ノード
        self.rank = [0] * N                # ランク
        self.diff_weight = [SUM_UNITY] * N 
    
    # 経路圧縮
    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            r = self.root(self.par[x])
            self.diff_weight[x] += self.diff_weight[self.par[x]]
            self.par[x] = r
            return r

    # 経路圧縮＋重みを返す
    def weight(self, x):
        self.root(x)
        return self.diff_weight[x]
    
    # xとyが同じグループに属するか判定
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # xとyの属するグループを1つにまとめる
    def merge(self, x, y, w):
        w = w + self.weight(x) - self.weight(y)
        x = self.root(x)
        y = self.root(y)
        if x == y: 
            return False
        else:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
                w = -w
            elif self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.diff_weight[y] = w
            return True

    # xとyが同じグループにいるとき、xとyの重みの差を返す
    def diff(self,x,y):
        return self.weight(y) - self.weight(x)


if __name__ == "__main__":
    _in = [_.rstrip() for _ in stdin.readlines()]
    N, M = list(map(int,_in[0].split(' ')))  # type:list(int)
    
    if M == 0:
        TF = 'Yes'
    else:
        L_R_D_arr = []
        for i in range(M):
            _ = list(map(int,_in[i+1].split(' ')))  # type:list(int)
            L_R_D_arr.append(_)
        # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        TF = 'No'
        wuf = Weighted_Union_Find(N)
        for L,R,D in L_R_D_arr:
            L -= 1
            R -= 1
            if wuf.issame(L,R):
                diff = wuf.diff(L,R)
                if diff != D:
                    break
            else:
                wuf.merge(L,R,D)
        else:
            TF = 'Yes'
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(TF)
