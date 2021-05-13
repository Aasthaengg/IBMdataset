from string import ascii_lowercase
import sys
input=sys.stdin.readline
s=input().rstrip()
t=input().rstrip()
for alp in ascii_lowercase:
    switch=0
    for i in range(len(s)):
        if switch==0:
            if s[i]==alp:
                rem=t[i]
                switch=1
        else:
            if s[i]==alp:
                if t[i]!=rem:
                    print("No")
                    exit()
for alp in ascii_lowercase:
    switch=0
    for i in range(len(s)):
        if switch==0:
            if t[i]==alp:
                rem=s[i]
                switch=1
        else:
            if t[i]==alp:
                if s[i]!=rem:
                    print("No")
                    exit()
print("Yes")