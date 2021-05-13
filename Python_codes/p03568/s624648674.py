N = int(input())
A = list(map(int,input().split()))
ALL = 3**N
even_count = 0
for a in A:
    if a%2 == 0:
        even_count += 1
print(ALL-2**even_count)