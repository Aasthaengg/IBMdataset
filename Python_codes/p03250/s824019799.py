abc = input()
abc_lis_str = abc.split()
abc_lis_int = [int(i) for i in abc_lis_str]
abc_lis = sorted(abc_lis_int, reverse=True)
a = abc_lis[0]
b = abc_lis[1]
c = abc_lis[2]

print( a * 10 + b + c )