H,W = map(int, input().split())

S_array = [["#" for _ in range(W+2)]] + [["#"] + list(input()) + ["#"] for i in range(H)] + [["#" for _ in range(W+2)]]

def connection_check(target_list):
    connection = 0
    connection_list = list()
    
    for i in range(len(target_list)):
        if target_list[i]=="#":
            connection_list += [connection for _ in range(connection)]
            connection_list += [0]
            connection = 0
        elif target_list[i]==".":
            connection += 1
    
    return connection_list

W_connection_array = [[0 for _ in range(W+2)]] + [connection_check(S_array[i]) for i in range(1,H+1)] + [[0 for _ in range(W+2)]]
H_connection_array = [[0 for _ in range(H+2)]] + [connection_check([row[i] for row in S_array]) for i in range(1,W+1)] + [[0 for _ in range(H+2)]]

#print(W_connection_array)
#print(H_connection_array)

ans = 0

for i in range(1,H+1):
    for j in range(1,W+1):
        temp_ans = W_connection_array[i][j] + H_connection_array[j][i]
        if ans < temp_ans:
            ans = temp_ans

print(ans - 1) #自分自身の分の重複加算を引く