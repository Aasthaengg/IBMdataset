n=int(input())
rate=380000
ans=0
for i in range(n):
    xi,ui=input().split()
    if ui=='JPY':
        ans+=int(xi)
    else:
        ans+=float(xi)*rate
print(ans)