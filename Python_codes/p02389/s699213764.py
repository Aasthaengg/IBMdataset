data = input()
len = data.split()
ans0 = int(len[0]) * int(len[1])
ans1 = int(len[0]) *2 + int(len[1])*2
print('{0} {1}'.format(ans0, ans1))