A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0

#　これだとダメ
# for a in range(A+1):
#     x = X - a*500
#     for b in range(B+1):
#         x -= b*100
#         for c in range(C+1):
#             x -= c*50
#             print(a,b,c,x)
#             if x == 0:
#                 ans += 1

# これはOK
# for a in range(A+1):
#     for b in range(B+1):
#         for c in range(C+1):
#             if 500*a+100*b+50*c == X:
#                 ans += 1


# こう書くとfor文一回省ける

for a in range(A+1):
    for b in range(B+1):
        x = X - 500*a -100*b

        if x%50 == 0 and x >=0:
            if x//50 <= C:
                ans += 1

print(ans)

#
