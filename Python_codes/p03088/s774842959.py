mod = 1000000007
n = int(input())
end_a = [0,0,0,16]
end_g = [0,0,0,15]
end_ag = [0,0,0,4]
end_ac = [0,0,0,3]
end_ga = [0,0,0,4]
end_at = [0,0,0,4]
end_aga = [0,0,0,1]
end_agt = [0,0,0,1]
end_agg = [0,0,0,1]
end_atg = [0,0,0,1]
ans = [0,0,0,61]
for i in range(3, n+1):
    end_a.append(ans[i]%mod)
    end_g.append((ans[i] - end_ac[i])%mod)
    end_ag.append(end_a[i]%mod)
    end_ac.append((end_a[i] - end_ga[i])%mod)
    end_ga.append(end_g[i]%mod)
    end_at.append(end_a[i]%mod)
    end_agt.append(end_ag[i]%mod)
    end_agg.append(end_ag[i]%mod)
    end_atg.append(end_at[i]%mod)
    taboo = (end_ag[i] + end_ac[i] + end_ga[i] + end_agt[i] + end_agg[i] + end_atg[i])%mod
    ans.append((taboo*3 + (ans[i]-taboo)*4)%mod)
print(ans[n]%mod)