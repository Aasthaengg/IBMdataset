N = int(input())
A_list = [int(e) for e in input().split()]

even_cnt = 0
odd_cnt = 0

for A in A_list:
    if A%2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1
        
#偶数の和は偶数
#奇数の和は偶数
#∴奇数の個数が偶数→偶数1個に縮まる→偶数は何個あっても最終的に偶数1個になるのでYES
#∴奇数の個数が奇数→奇数1個偶数1個に縮まる→NG(ただし1個かつ偶数0個なら特例OK)

if (odd_cnt == 1 and even_cnt == 0)or(odd_cnt%2==0):
    print("YES")
else:
    print("NO")