n, m = map(int, input().split())

# flip odd or even
# check concatinated mass
# if that odd, it will back. if even, be opposite.
# ans=0
# for i in range(n):
#     for j in range(m):
#         c=0
#         for h in range(-1,2):
#             for w in range(-1,2):
#                 if 0<i+h<n-1 and 0<j+w<m-1:
#                     c+=1
#         if c%2==1:
#             ans+=1
# print(ans, flush=True)
# TLE


ans=0
if n==1 and m==1:
    print(1, flush=True)
elif n==1 or m==1:
    print(max(n-2, m-2), flush=True)
else:
    print((n-2)*(m-2))
