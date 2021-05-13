N=int(input())
trans=min([int(input()) for _ in range(5)])
ans=(N+(trans-1))//trans+4
print(ans)