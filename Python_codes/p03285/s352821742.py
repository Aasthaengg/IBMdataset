N = int(input())

P = [(a,b) for a in range(N//4+1) for b in range(N//7+1) if 4*a + 7*b == N]

print('No' if len(P)==0 else 'Yes')