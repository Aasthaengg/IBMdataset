N = int(input())
S = input()

tot = S[1:].count('E')
tot_list = [tot]
former_leader = S[0]

for l in range(1, N):
    leader = S[l]
    if (former_leader, leader)  == ('E', 'E'):
        tot -= 1
    if (former_leader, leader)  == ('W', 'W'):
        tot += 1
        
    former_leader = leader  
    tot_list.append(tot)
    
print(min(tot_list))