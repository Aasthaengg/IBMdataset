#coding:utf-8

n1 , n2 =input().rstrip().split(" ")

if int(n1)<int(n2):
    print("a < b")

elif int(n1)==int(n2):
    print("a == b")


else:
    print("a > b")