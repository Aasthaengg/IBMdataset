#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 問題：https://atcoder.jp/contests/abc126/tasks/abc128_b

N = int(input())
numbers = []
cities = []
points = []

for i in range(N):
    city, point = input().split()
    numbers.append(i+1)
    cities.append(city)
    points.append(int(point))

def switch_order(l, i, j):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp

for i in range(N):
    for j in range(i):
        if cities[j] < cities[i]:
            continue
        if cities[j] > cities[i]:
            switch_order(numbers, i, j)
            switch_order(cities, i, j)
            switch_order(points, i, j)
        if cities[j] == cities[i] and points[j] < points[i]:
            switch_order(numbers, i, j)
            switch_order(cities, i, j)
            switch_order(points, i, j)

for i in range(N):
    print(numbers[i])
