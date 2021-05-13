n = int(input())
li = [0 for i in range(n)]

def call(num):
    print(num,flush=True)

def responce(num):
    res = input()
    if res == "Vacant":
        exit()
    elif res == "Male":
        li[num] = 1
    else:
        li[num] = 2
    
call(0)
responce(0)
call(n-1)
responce(n-1)
l = 0
r = n-1
while True:
    m = (r+l)//2
    call(m)
    responce(m)
    if ((m-l+1)%2 == 1 and li[m] != li[l]) or ((m-l+1)%2 == 0 and li[m] == li[l]):
        r = m
    else:
        l = m