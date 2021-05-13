#Boost Force  / Backtracking
import sys
input = sys.stdin.readline
d = []
f = []
time = 0
#ทำการ search
def search(r):
    global d,f,time,s
    if d[r] == 0:
        time += 1
        d[r] = time
    else:
        return
    for x in s[r]:
        search(x)
    time += 1
    f[r] = time


n = int(input()) #รับค่าจำนวน node ทั้งหมด
s = [[] for i in range(n+1)]
for _ in range(n):
    d = list(map(int,input().split())) #รับข้อมูลทีละบรรทัด split เก็บเป็น int
    #ตน d[0] คือ node ตน 1 คือ ดีกรี ตนตั้งแต่ 2ไป คือ vertex
    s[d[0]] = d[2:]

d = [0 for _ in range(n+1)]
f = [0 for _ in range(n+1)]

for i in range(1,n+1):
    if d[i] == 0:
        search(i)

#แสดง node เวลาที่เจอ และ เวลา finish
for i in range(1,n+1):
    print (i,d[i],f[i])

