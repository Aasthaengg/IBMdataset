#coding:utf-8

a , b =[int(i) for i in input().split(" ")]

print(str(a//b) +" "+str(a%b) +" "+"{0:.5f}".format(a/b))