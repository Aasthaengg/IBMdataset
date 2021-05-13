#!/usr/bin/env python3

s=input()

hi="hi"

if len(s)%2==0:
    if s == "hi"*int(len(s)/2):
        print("Yes")
    else:
        print("No")
else:
    print("No")


