n=int(input())
a=[int(x) for x in input().split()]

deno=0
for i in a:
    deno+=1/i
print(1/deno)