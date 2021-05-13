def judge_status_summary():
    N = int(input())
    res = {"AC":0,"WA":0,"TLE":0,"RE":0}
    for i in range(N):
        res[input()] += 1
    
    for k in res:
        print("{} x {}".format(k,res[k]))
        
judge_status_summary()