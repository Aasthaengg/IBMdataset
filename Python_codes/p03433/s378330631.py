import sys

n = int(input())
a = int(input())

amari = n % 500

print("Yes") if amari <= a else print("No")