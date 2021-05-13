S=input();
K=input();
i = 0;
for i in range(len(S)) :
    if int(S[i]) > 1 :
        print(S[i]);
        break;
    elif i + 1 >= int(K) :
        print(1);
        break;
