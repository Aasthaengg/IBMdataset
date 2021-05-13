S_list = list(map(int,input().split()))
A,B,C,D = S_list
takahashi ,aoki = A, C
while takahashi > 0 or aoki > 0:
    aoki = aoki - B
    if aoki <=0 :
        break
    takahashi = takahashi - D
    if takahashi <=0:
        break
        """
    print("あおき:"+str(aoki))
    print("たかはし:"+str(takahashi))
		"""
if takahashi > aoki:
    result = "Yes"
else:
    result = "No"
print(result)