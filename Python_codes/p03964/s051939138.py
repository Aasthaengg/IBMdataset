n = int(input())

t_vote = 1
a_vote = 1

for _ in range(n):
    t,a = map(int,input().split())
    if t_vote*a > a_vote*t:
        t_vote = (t_vote + t-1)//t*t
        a_vote = t_vote//t*a
    else:
        a_vote = (a_vote + a-1)//a*a
        t_vote = a_vote//a*t
print(t_vote+a_vote)