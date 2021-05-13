N = input()
count0 = N.count('0')
count1 = len(N)-count0
print(min(count0,count1)*2)