P,Q,R=map(int,input().split())
if (1<=P&P<=100)&(1<=Q&Q<=100)&(1<=R&R<=100):
    ABC=P+Q
    BCA=Q+R
    CAB=R+P
    answer=min(ABC,BCA,CAB)
    print(answer)