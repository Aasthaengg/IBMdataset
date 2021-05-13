#condig: UTF-8
import sys
n = int(raw_input())
        
while True:
    try :
        a = sorted(map(int,raw_input().split()))
        print "YES" if a[0] ** 2 + a[1] ** 2 == a[2] ** 2 else "NO"
    except:
        break