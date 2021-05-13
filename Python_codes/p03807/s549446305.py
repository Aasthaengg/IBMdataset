N = int(input())
A_list = list(map(int,input().split()))

# A_listのうち、奇数であるA_Nが偶数個ならばYES, 奇数個ならばNOである。
modsum = 0
for i in A_list:
    modsum += i % 2

if modsum % 2 == 0:
    print("YES")
else:
    print("NO")