a,b,c = input().split()
a_len=len(a)
b_len=len(b)

print('YES' if a[a_len-1]==b[0] and b[b_len-1]==c[0] else 'NO')