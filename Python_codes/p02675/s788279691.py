n = int(input())
hon = [2,4,5,7,9]
pon = [0,1,6,8]
bon = [3]

print("hon" if n%10 in hon else "pon" if n%10 in pon else "bon")