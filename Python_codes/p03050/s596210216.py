N=int(input())
div = []
ans = 0
for i in range(1,int(pow(N,0.5)+3)):
    if N%i==0:
        div.append(i)
        div.append(N//i)
div = list(set(div))
for i in map(lambda x:x-1,div):
    if i != 0 and N%i==N//i:
        ans += i
print(ans)