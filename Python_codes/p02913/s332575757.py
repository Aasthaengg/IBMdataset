"""
X文字が条件にあてはまるとき、X-1文字も条件に当てはまる。したがって、二分探索を使うのがよい。
一回の探索に、O(N**2)かかる。
探索はO(logN)回行うため、全体でO(N**2logN)で、ギリ間に合う。
"""
N = int(input())
S = input()

def is_ok(X):
    dic = {}
    for i in range(N+1-X):
        sub = S[i:i+X]
        if sub not in dic:
            dic[sub] = (i,i+X-1)
        else:
            if dic[sub][1] < i:
                return True
    return False

def bisearch(high,low):
    while high - low > 1:
        mid = (high+low)//2
        if is_ok(mid):
            low = mid
        else:
            high = mid
    return low
print(bisearch(N,0))