# coding: utf-8

num = input().rstrip().split(" ")

ishow = int(num[0]) // int(num[1])
amari = int(num[0]) % int(num[1])
fshow = float(int(num[0])) / int(num[1])

print(str(ishow) + " " + str(amari) + " " + str("{0:.5f}".format(fshow)))