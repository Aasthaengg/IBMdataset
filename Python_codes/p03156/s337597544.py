N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))
first = [p for p in P if p<=A]
second = [p for p in P if p>A and p<=B]
third = [p for p in P if p>B]

ans = min(len(first),len(second),len(third))

print(ans)   

#print(*ans, sep='\n')
