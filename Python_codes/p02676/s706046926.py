#Kは 1 以上 100以下の整数
#Sは英小文字からなる文字列
#Sの長さは1以上100以下

k = int(input())
s =input()

if len(s) <= k: #Sの長さがKまで
    print(s)
else:
    s = s[:k]
    s = s+"... "
    print(s)