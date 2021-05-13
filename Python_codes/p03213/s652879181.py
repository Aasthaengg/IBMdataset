import itertools
def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = [2]
    limit = int(n**0.5) #ルートn以上で割れることはない
    data = [i + 1 for i in range(2, n, 2)] #最初から3スタートの奇数にしておく
    while True:
        p = data[0]
        if limit < p: #ここでイコールが入るとlimitが素数の時にlimit^2が残ってダメ。
            return prime + data
        prime.append(p) #ここで一番最初に取り出した素数を加える。
        data = [e for e in data if e % p != 0] #残りでその素数で割れない数字を取得。

Sosu = get_sieve_of_eratosthenes(100)
#print(Sosu)
N = int(input())
limit = 1
for i in range(N):
  limit *= i+1
ans = 0
A = [0]*len(Sosu)
for i in range(1,N+1):
  now = i*1
  for j in range(len(Sosu)):
    while now%Sosu[j] == 0:
      A[j] += 1
      now //= Sosu[j]
    if now == 1:
      break
#print(A)
ans = 0
for i in A:
  if i >= 74:
    ans +=1
T = list(itertools.permutations(A,2)) #順列
for L in T:
  first,second = L
  if first >= 4 and second >= 14:
    ans += 1
  if first >= 2 and second >= 24:
    ans += 1
T = list(itertools.permutations(A,3)) #順列
#print(T)
temp = 0
for L in T:
  first,second,third = L
  if first >= 2 and second >= 4 and third >= 4:
    temp += 1
temp = temp//2
ans += temp
print(ans)