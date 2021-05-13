ali = []
for i in range(52):
    if i <= 25:
        ali.append(chr(ord("A")+i))
    else:
        ali.append(chr(ord("A")+i-26))
#ここから
n = int(input())
s = input()
news = ""
for i in range(len(s)):
    news += ali[ali.index(s[i]) + n]
print(news)