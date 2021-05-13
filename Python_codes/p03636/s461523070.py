s = str(input())

count = 0

for i in s:
    count +=1

print("{}{}{}".format(s[0], count-2, s[-1]))