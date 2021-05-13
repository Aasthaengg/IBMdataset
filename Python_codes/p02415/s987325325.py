# coding: utf-8

print("".join(i.upper() if i.islower() else i.lower() for i in input()))