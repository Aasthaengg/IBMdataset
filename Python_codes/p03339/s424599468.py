"""
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iomanip>
int main()
{
    long N;
    std::cin >> N;
    std::string S;
    std::cin >> S;
    long count=0;
    std::vector<long> counters;
    for(long i=1; i<N; i++){
        if(S[i]=='E'){
            count++;
        }
    }
    counters.push_back(count);
    for(long i=1; i<N; i++){
        if(S[i]=='E'){
            count-=1;
        }
        if(S[i-1]=='W'){
            count++;
        }
        counters.push_back(count);
    }
    std::sort(counters.begin(),counters.end());
    std::cout << counters[0] << std::endl;
    return 0;
}
"""
n=int(input())
s=input()
cnt=0
for i in range(1,n):
  if s[i]=="E":cnt+=1
ans=[]
ans.append(cnt)
for i in range(1,n):
  if s[i]=="E":
    cnt-=1
  if s[i-1]=="W":
    cnt+=1
  ans.append(cnt)
print(min(ans))
