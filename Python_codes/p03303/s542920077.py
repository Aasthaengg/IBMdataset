import math
s = input()
n = int(input())
news = ""
c = math.ceil(len(s)/n)
for i in range(c):
    news += s[(i)*n]
print(news)