a, b, c, k = map(int, input().split())

# for _ in range(k):
#         tmpA = a
#         tmpB = b
#         tmpC = c
#         a = tmpB + tmpC
#         b = tmpA + tmpC
#         c = tmpB + tmpA
#         if a - b >= 10**18:
#             print("Unfair")
#             exit()
# 
# print(a - b)
if a-b >= 10**18 or b-a >= 10**18:
    print("Unfair")
    exit()

if k%2 == 0:
    print(a-b)
else:
    print(b-a)