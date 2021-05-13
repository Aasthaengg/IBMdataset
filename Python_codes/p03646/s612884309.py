k=int(input())
print(50)
p=k//50
q=k%50
ans=[49-(q-1)+p+50]*q+[49-q+p]*(50-q)
print(*ans)