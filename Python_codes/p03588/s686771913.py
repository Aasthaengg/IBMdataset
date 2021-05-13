N=int(input())
AB=[tuple(map(int, input().split())) for _ in range(N)]

max_a=0
max_b=0
for a,b in AB:
    if max_a<a:
        max_a=a
        max_b=b
print(max_b+max_a)