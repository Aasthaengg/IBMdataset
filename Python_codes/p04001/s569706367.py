S = input()
n = len(S)
import copy

ans = [0]

def rec(index,tmp,tmp_list):
    # print(tmp,tmp_list)
    if index > n-1:

        tmp_list.append(tmp)
        # print(tmp_list)
        # print(tmp_list)
        ans[0] += sum(tmp_list)
        return

    tmp_list1 = copy.deepcopy(tmp_list)
    tmp_list2 = copy.deepcopy(tmp_list)
    
    
    tmp_list1.append(tmp)
    rec(index+1,int(S[index]),tmp_list1)

    rec(index+1,10*tmp + int(S[index]),tmp_list2)
    return

rec(1,int(S[0]),[])
print(ans[0])