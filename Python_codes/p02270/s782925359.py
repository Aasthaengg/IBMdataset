#???
n,k = map(int,input().split())
l=[int(input()) for _ in range(n)]

def check(p):
    j=0
    for _ in range(k):
        sum=0
        """
        if l[j]>p: #そもそもある一個の荷物の重さがpを超える場合
            return False #j=0の瞬間から引っかかったとしてもwhileには入らないので、k回ループの後どうせfalseになる
            """
        while sum+l[j] <= p:
            sum+=l[j]
            j+=1
            if j==n:
                return True
    return False

#binarysearch
L=0
R=10000*100000
ans=0
while L<=R:
    M = (L+R) // 2
    if check(M):
        ans=M
        R=M-1#最終的にこの行のRを答えとして出そうとすると、実際の最小値より下回ってしまうことがあるので注意。
            #この行は次のbinarysearchに進む前提で更新しているのでこれを出力しない
    else:
        L=M+1
print(ans)


# もし，仮に，Pが決まっていたら前から貪欲にギリギリまで物を詰めるのが最適
# そうすることで必要なトラックの数を最小に抑えることができる
#
"""
#include <iostream>

using namespace std;

#define rep(i, n) REP(i,0,n)
#define REP(i,a,n) for(int i = a ; i < (int)n ; i++)

typedef long long ll;

int n, k;
int w[100001];
#二分探索を進めてPの最小値を決定する
bool check(int p){ #Pの値を二分探索して，判定関数はそのPの値でk台以内で荷物を積み切れるか
  #を判定、積み切れるならtrue->さらに小さい値からPを探す(right(最大値)を小さくする)。
  # 積み切れないならfalse->さらに大きい値からPを探す(left(最小値))を大きくする。
  ll sum=0;
  int idx = 0;

  rep(i, k){#k台以内に全ての荷物を積み切れるか？
    sum = 0;
    while(w[idx] + sum <= p){#k以内ならwhileは何回入ってもいい、入り直すたびにトラックが新しくなる(sum=0にする)
      sum+=w[idx];
      idx++;
      if(idx == n) return true;
    }
  }
  return false;
}

signed main(){
  cin >> n >> k;

  rep(i, n) cin >> w[i];
  
  // binary search
  ll left = 0, right = 100000 * 10000;#もしトラックの数が１台しかなければ全ての荷物が最大重量の場合(w_i=10000)をその最大個数分(n=100000)積めなくてはならないのでこれがPの最悪計算量(最大値)
  while(right - left > 1){
    ll mid = (left + right) / 2;
    if(check(mid)) right = mid;
    else left = mid;
  }
  
  cout << right << endl;
}
"""
