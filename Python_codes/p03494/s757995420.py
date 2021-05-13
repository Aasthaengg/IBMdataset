am = int(input())
arr = list(map(int,input().split()))
out = [0]*am
for i in range(am):
  while arr[i]&1 == 0:
    out[i]+=1
    arr[i]= arr[i]//2
print(min(out))