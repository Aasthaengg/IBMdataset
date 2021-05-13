# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
#      .      '                    Udit Gupta @luctivud         ,              
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            ##     ##  #######  # #  ######
                            ##     ##  ##   ##  ###    ##
                            ##     ##  ##    #  # #    ##
                            #########  #######  # #    ##
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import sys
import math
# sys.setrecursionlimit(10**6)

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))

def printwsp(*args): return print(*args, end="")
def printsp(*args): return print(*args, end=" ")
def printchk(*args): return print(*args, end="tst, ")

MODPRIME = int(1e9+7); BABYMOD = 998244353;
# ################################ HELPER PROGRAMS USED ###################################
# ################################## MAIN STARTS HERE #####################################
# for _testcases_ in range(int(input())):
ans = 'No'
s = input()
if len(s)==6 and s[0] != s[1] and s[2] == s[3] and s[4] == s[5]:
    ans = "Yes"
print(ans)


# #########################################################################################
'''
THE LOGIC AND APPROACH IS BY ME @luctivud.
SOME PARTS OF THE CODE HAS BEEN TAKEN FROM WEBSITES LIKE::
(I Own the code if no link is provided here or I may have missed mentioning it)
: DO NOT PLAGIARISE.
'''