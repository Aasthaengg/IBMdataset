a,b = map(int,input().split())

arr = []#素数リスト　(素数:べき)の形で出てくる

def factorization(n):
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

factorization(a)
ans = 0

for p,n in arr:
  if b%p == 0:
    ans += 1
    
if len(arr) == 1 and arr[0][0] == 1:
  print(1)
  exit()
  
print(ans+1)