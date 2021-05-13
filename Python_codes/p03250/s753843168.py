A, B, C = input().split()

ans = []

ans.append(int(A) + int(B+C))
ans.append(int(A) + int(C+B))
ans.append(int(B) + int(A+C))
ans.append(int(B) + int(C+A))
ans.append(int(C) + int(A+B))
ans.append(int(C) + int(B+A))

print(max(ans))