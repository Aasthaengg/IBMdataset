#!/usr/bin python3
# -*- coding: utf-8 -*-

def factorization(n):
    primen, degree, primend = [], [], []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            primen.append(i)
            degree.append(cnt)
            primend.append([i,cnt])
    if temp!=1:
        primen.append(temp)
        degree.append(1)
        primend.append([temp,1])
    if primen==[]:
        primen.append(n)
        degree.append(1)
        primend.append([n,1])
    return primend

N = int(input())
pm = [0]*(1+N)

def main():
    for i in range(1,N+1):
        for x in factorization(i):
            pm[x[0]]+=x[1]
    ret = 1
    for j in pm[2:]:
        ret *= j+1
        ret %= 1000000007
    print(ret)

if __name__ == '__main__':
    main()