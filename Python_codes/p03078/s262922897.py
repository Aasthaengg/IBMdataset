x, y, z, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
 
AB = [a + b for a in A for b in B]
AB.sort(reverse=True)
AB = AB[:k]
 
ABC = [ab + c for ab in AB for c in C]
ABC.sort(reverse=True)
ABC = ABC[:k]
 
print('\n'.join(map(str, ABC)))